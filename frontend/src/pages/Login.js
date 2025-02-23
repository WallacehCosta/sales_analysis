import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Button from "../components/Button";
import authService from "../services/authService";

const Login = () => {
  const navigate = useNavigate();

  // Estados para armazenar os dados do formulário e mensagens de erro
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  // Função para lidar com o login
  const handleLogin = async (e) => {
    e.preventDefault(); // Evita o recarregamento da página

    // Validação básica dos campos
    if (!email || !password) {
      setError("Por favor, preencha todos os campos.");
      return;
    }

    try {
      // Chama o serviço de autenticação para fazer login
      const user = await authService.login(email, password);

      // Se o login for bem-sucedido, redireciona para o dashboard
      if (user) {
        navigate("/dashboard");
      }
    } catch (error) {
      // Exibe mensagem de erro em caso de falha no login
      setError("Email ou senha incorretos. Tente novamente.");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded-lg shadow-md w-96">
        <h2 className="text-2xl font-bold mb-6 text-center">Login</h2>

        {/* Exibe mensagem de erro, se houver */}
        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-2 rounded mb-4">
            {error}
          </div>
        )}

        <form onSubmit={handleLogin}>
          <div className="mb-4">
            <label className="block text-sm font-medium mb-2" htmlFor="email">
              Email
            </label>
            <input
              type="email"
              id="email"
              className="w-full p-2 border border-gray-300 rounded-lg"
              placeholder="Digite seu email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div className="mb-6">
            <label className="block text-sm font-medium mb-2" htmlFor="password">
              Senha
            </label>
            <input
              type="password"
              id="password"
              className="w-full p-2 border border-gray-300 rounded-lg"
              placeholder="Digite sua senha"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <Button type="submit" className="w-full">
            Entrar
          </Button>
        </form>
      </div>
    </div>
  );
};

export default Login;