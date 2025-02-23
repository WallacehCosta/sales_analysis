import api from "./api";

const authService = {
  // Função para fazer login
  login: async (email, password) => {
    try {
      const response = await api.post("/auth/login", { email, password });
      localStorage.setItem("token", response.data.access_token); // Salva o token no localStorage
      return response.data;
    } catch (error) {
      throw error.response ? error.response.data : error.message;
    }
  },

  // Função para fazer logout
  logout: () => {
    localStorage.removeItem("token"); // Remove o token do localStorage
  },

  // Função para verificar se o usuário está autenticado
  isAuthenticated: () => {
    const token = localStorage.getItem("token");
    return !!token; // Retorna true se o token existir
  },
};

export default authService;
