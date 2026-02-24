

import React, { useState } from 'react';
import './App.css';


function App() {
  const [messages, setMessages] = useState([
    {
      sender: 'ai',
      text: 'Hi! Ask me anything about industrial incidents.',
    },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;
    setLoading(true);
    setError("");
    const userMsg = { sender: 'user', text: input };
    setMessages((msgs) => [...msgs, userMsg]);
    setInput("");
    try {
      const response = await fetch("http://localhost:8000/explain-incident", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question: userMsg.text }),
      });
      if (!response.ok) {
        throw new Error("API error");
      }
      const data = await response.json();
      setMessages((msgs) => [
        ...msgs,
        { sender: 'ai', text: data.explanation },
      ]);
    } catch (err) {
      setError("Failed to fetch explanation.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="ChatApp">
      <div className="ChatHeader">AI Incident Chat</div>
      <div className="ChatBody">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`ChatBubble ${msg.sender === 'user' ? 'UserBubble' : 'AIBubble'}`}
          >
            <div className="Avatar">
              {msg.sender === 'user' ? (
                <span role="img" aria-label="user">🧑</span>
              ) : (
                <span role="img" aria-label="ai">🤖</span>
              )}
            </div>
            <div className="BubbleText">{msg.text}</div>
          </div>
        ))}
        {loading && (
          <div className="ChatBubble AIBubble">
            <div className="Avatar"><span role="img" aria-label="ai">🤖</span></div>
            <div className="BubbleText">Typing...</div>
          </div>
        )}
        {error && <div className="ErrorMsg">{error}</div>}
      </div>
      <form className="ChatInputBar" onSubmit={handleSubmit} autoComplete="off">
        <input
          type="text"
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Type your question..."
          disabled={loading}
        />
        <button type="submit" disabled={loading || !input.trim()}>
          Send
        </button>
      </form>
    </div>
  );
}

export default App;
