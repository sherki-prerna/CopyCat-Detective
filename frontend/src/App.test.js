import { render, screen } from '@testing-library/react';
import App from './App';

test('renders copycat app shell', () => {
  render(<App />);
  expect(screen.getByText(/CopyCat Detective/i)).toBeInTheDocument();
  expect(screen.getByText(/Analyze Similarity/i)).toBeInTheDocument();
});
