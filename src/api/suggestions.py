import { api } from "./axios";

export async function fetchSuggestions() {
  const { data } = await api.get("/suggestions");
  return data as { symbol: string; category: string }[];
}
