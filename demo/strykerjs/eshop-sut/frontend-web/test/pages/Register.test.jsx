import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import axios from 'axios';
import Register from '../../src/pages/Register';

vi.mock('axios', () => ({
  default: {
    post: vi.fn(),
  },
}));

const ERROR_TEXT = /Mật khẩu quá yếu/i;
const VALID_PASSWORD = 'Abcdef1 '; // upper + lower + digit + whitespace, exactly 8 chars

function renderRegister() {
  const utils = render(
    <MemoryRouter>
      <Register />
    </MemoryRouter>,
  );
  const [nameInput, emailInput] = utils.container.querySelectorAll('input[type="text"]');
  const passwordInput = utils.container.querySelector('input[type="password"]');
  const form = utils.container.querySelector('form');
  return { ...utils, nameInput, emailInput, passwordInput, form };
}

function submitPassword(value) {
  const { passwordInput, form } = renderRegister();
  fireEvent.change(passwordInput, { target: { value } });
  fireEvent.submit(form);
}

describe('Register - password validation', () => {
  it('starts every field empty and shows no error box before submitting', () => {
    const { nameInput, emailInput, passwordInput, container } = renderRegister();
    expect(nameInput).toHaveValue('');
    expect(emailInput).toHaveValue('');
    expect(passwordInput).toHaveValue('');
    expect(container.querySelector('.bg-red-100')).toBeNull();
  });

  it('rejects an empty/short password', () => {
    submitPassword('abc');
    expect(screen.getByText(ERROR_TEXT)).toBeInTheDocument();
  });

  it('rejects a password missing an uppercase letter', () => {
    submitPassword('abcdefg1 ');
    expect(screen.getByText(ERROR_TEXT)).toBeInTheDocument();
  });

  it('rejects a password missing a lowercase letter', () => {
    submitPassword('ABCDEFG1 ');
    expect(screen.getByText(ERROR_TEXT)).toBeInTheDocument();
  });

  it('rejects a password missing a digit', () => {
    submitPassword('Abcdefgh ');
    expect(screen.getByText(ERROR_TEXT)).toBeInTheDocument();
  });

  it('rejects a password missing whitespace', () => {
    submitPassword('Abcdefg1');
    expect(screen.getByText(ERROR_TEXT)).toBeInTheDocument();
  });

  it('rejects a password shorter than 8 characters even if all character classes are present', () => {
    submitPassword('Ab1 cde'); // 7 chars, has upper/lower/digit/space
    expect(screen.getByText(ERROR_TEXT)).toBeInTheDocument();
  });

  it('accepts a password that satisfies every requirement (8 chars, boundary case)', async () => {
    axios.post.mockResolvedValue({ data: {} });
    const { nameInput, emailInput, passwordInput, form } = renderRegister();

    fireEvent.change(nameInput, { target: { value: 'Nguyen Van A' } });
    fireEvent.change(emailInput, { target: { value: 'a@example.com' } });
    fireEvent.change(passwordInput, { target: { value: VALID_PASSWORD } });
    fireEvent.submit(form);

    await waitFor(() =>
      expect(axios.post).toHaveBeenCalledWith('http://localhost:3000/api/register', {
        name: 'Nguyen Van A',
        email: 'a@example.com',
        password: VALID_PASSWORD,
      }),
    );
    expect(screen.queryByText(ERROR_TEXT)).not.toBeInTheDocument();
  });

  it('updates the name and email fields when typed into', () => {
    const { nameInput, emailInput } = renderRegister();
    fireEvent.change(nameInput, { target: { value: 'Nguyen Van A' } });
    fireEvent.change(emailInput, { target: { value: 'a@example.com' } });
    expect(nameInput).toHaveValue('Nguyen Van A');
    expect(emailInput).toHaveValue('a@example.com');
  });
});
