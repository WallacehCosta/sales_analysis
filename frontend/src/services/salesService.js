import api from "./api";

const salesService = {
  // Função para buscar todas as vendas
  getSales: async () => {
    try {
      const response = await api.get("/sales");
      return response.data;
    } catch (error) {
      throw error.response ? error.response.data : error.message;
    }
  },

  // Função para buscar uma venda específica por ID
  getSaleById: async (id) => {
    try {
      const response = await api.get(`/sales/${id}`);
      return response.data;
    } catch (error) {
      throw error.response ? error.response.data : error.message;
    }
  },

  // Função para criar uma nova venda
  createSale: async (saleData) => {
    try {
      const response = await api.post("/sales", saleData);
      return response.data;
    } catch (error) {
      throw error.response ? error.response.data : error.message;
    }
  },
};

export default salesService;
