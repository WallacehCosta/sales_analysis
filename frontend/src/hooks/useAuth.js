import { useState, useEffect } from "react";
import authService from "../services/authService";

const useAuth = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(authService.isAuthenticated());

  // Função para fazer login
  const login = async (email, password) => {
    try {
      const user = await authService.login(email, password);
      setIsAuthenticated(true);
      return user;
    } catch (error) {
      setIsAuthenticated(false);
      throw error;
    }
  };

  // Função para fazer logout
  const logout = () => {
    authService.logout();
    setIsAuthenticated(false);
  };

  // Atualiza o estado de autenticação quando o token muda
  useEffect(() => {
    setIsAuthenticated(authService.isAuthenticated());
  }, []);

  return { isAuthenticated, login, logout };
};

export default useAuth;
