

import React, { useState } from 'react';

function RobotIcon({ thinking }) {
  return (
    <div className={thinking ? "robot-icon robot-thinking" : "robot-icon"}>
      <svg width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="18" cy="18" r="18" fill="#7c2b7a" />
        <ellipse cx="12" cy="16" rx="3" ry="4" fill="#fff" />
        <ellipse cx="24" cy="16" rx="3" ry="4" fill="#fff" />
        <ellipse cx="12" cy="16" rx="1.2" ry="1.5" fill="#7c2b7a" />
        <ellipse cx="24" cy="16" rx="1.2" ry="1.5" fill="#7c2b7a" />
        <rect x="12" y="24" width="12" height="2" rx="1" fill="#fff" />
      </svg>
      {thinking && <div className="robot-thinking-dots">
        <span>.</span><span>.</span><span>.</span>
      </div>}
    </div>
  );
}

function App() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([
    { sender: "ai", text: "Hi! Ask me anything about industrial incidents." }
  ]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setMessages(prev => [...prev, { sender: "user", text: question }]);
    try {
      const response = await fetch("http://localhost:8000/explain-incident", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question }),
      });
      if (!response.ok) {
        throw new Error("API error");
      }
      const data = await response.json();
      setMessages(prev => [...prev, { sender: "ai", text: data.explanation, time: data.answer_time_seconds }]);
    } catch (err) {
      setError("Failed to fetch explanation.");
      setMessages(prev => [...prev, { sender: "ai", text: "Sorry, I couldn't fetch an answer." }]);
    } finally {
      setLoading(false);
    }
    setQuestion("");
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <RobotIcon thinking={loading} />
        <span className="chat-title">AI Incident Explainer</span>
      </div>
      <div className="chat-box">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={
              msg.sender === "user" ? "chat-row chat-row-user" : "chat-row chat-row-ai"
            }
          >
            {msg.sender === "ai" && (
              <div className="chat-avatar ai-avatar">
                <RobotIcon thinking={false} />
              </div>
            )}
            <div className={msg.sender === "user" ? "chat-bubble user-bubble" : "chat-bubble ai-bubble"}>
              <span className="chat-sender">{msg.sender === "user" ? "You" : "AI"}</span>
              <span className="chat-text">{msg.text}</span>
              {msg.sender === "ai" && msg.time !== undefined && (
                <span className="chat-time">⏱ Answered in {msg.time}s</span>
              )}
            </div>
            {msg.sender === "user" && (
              <div className="chat-avatar user-avatar">
                <img src="https://cdn-icons-png.flaticon.com/512/1946/1946429.png" alt="User" />
              </div>
            )}
          </div>
        ))}
        {loading && (
          <div className="chat-bubble ai-bubble">
            <span className="chat-sender">AI</span>
            <span className="chat-text">Thinking...</span>
          </div>
        )}
      </div>
      <form className="chat-input-area" onSubmit={handleSubmit}>
        <input
          className="chat-input"
          type="text"
          value={question}
          onChange={e => setQuestion(e.target.value)}
          placeholder="Type your question..."
          required
          disabled={loading}
        />
        <button className="chat-send-btn" type="submit" disabled={loading}>
          <span role="img" aria-label="send">💬</span>
        </button>
      </form>
      {error && <div className="chat-error">{error}</div>}
    </div>
  );
}

export default App;
