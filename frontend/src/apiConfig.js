const ENV = "local"
const API_BASE_URL = ENV == "prod" ? 'https://bpaternostro.site/trader/api' : "http://localhost:8000/trader/api";

export const ROOT = "/trader"
export const API_ENDPOINTS = {
  financialInstruments:`${API_BASE_URL}/financial-instrument`,
  uploadImage: `${API_BASE_URL}/products/image-upload`,
  trader:`${API_BASE_URL}`,
  traderCreatePortfolio:`${API_BASE_URL}`,
  portofolios:`${API_BASE_URL}/portfolio`,
  portofoliosFinInstrument:`${API_BASE_URL}/portfolio-financial-instrument`,
  portofoliosFinInstrumentOperation:`${API_BASE_URL}/portfolio-financial-instrument-op`,
  portofoliosFinInstrumentUpdateStatus:`${API_BASE_URL}/portfolio-financial-instrument/update-ticker/`,
  portofoliosFinInstrumentMoveTicker:`${API_BASE_URL}/portfolio-financial-instrument/move-ticker/`,
  list:`${API_BASE_URL}/list-values`,
  // Add more endpoints as needed
};