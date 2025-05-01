import { useState } from "react";
import { login } from "../api/auth";

export function Login() {
  const [email, setEmail] = useState("");
  const [pw, setPw] = useState("");
  const [err, setErr] = useState("");

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    try {
      await login(email, pw);
      window.location.href = "/";
    } catch {
      setErr("Bad credentials");
    }
  }

  return (
    <main className="h-screen flex flex-col items-center justify-center gap-4">
      <h1 className="text-2xl font-bold">Stock Sage Login</h1>
      <form className="flex flex-col gap-2 w-72" onSubmit={submit}>
        <input
          className="border p-2 rounded"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          className="border p-2 rounded"
          type="password"
          placeholder="Password"
          value={pw}
          onChange={(e) => setPw(e.target.value)}
        />
        <button className="bg-blue-600 text-white rounded p-2">Login</button>
        {err && <p className="text-red-500">{err}</p>}
      </form>
    </main>
  );
}
