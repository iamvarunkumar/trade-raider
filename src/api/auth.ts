import { api } from "./axios";

export function login(email: string, password: string) {
  return api.post("/auth/login", { email, password });
}
