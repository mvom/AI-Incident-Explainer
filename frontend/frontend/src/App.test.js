import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import App from './App';

global.fetch = jest.fn(() =>
  Promise.resolve({
    ok: true,
    json: () => Promise.resolve({ explanation: 'Test explanation.' }),
  })
);

describe('Chat UI', () => {
  it('renders initial AI message', () => {
    render(<App />);
    expect(screen.getByText(/ask me anything/i)).toBeInTheDocument();
  });

  it('sends user message and receives AI response', async () => {
    render(<App />);
    const input = screen.getByPlaceholderText(/type your question/i);
    fireEvent.change(input, { target: { value: 'Hello?' } });
    fireEvent.click(screen.getByText(/send/i));
    await waitFor(() => expect(screen.getByText('Test explanation.')).toBeInTheDocument());
  });
});

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
