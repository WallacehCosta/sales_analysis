import axios from "axios";

// Configuração base do Axios
const api = axios.create({
  baseURL: "http://localhost:8000/api", // Ajustável
  headers: {
    "Content-Type": "application/json",
  },
});

// Interceptador para adicionar o token JWT às requisições
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;
