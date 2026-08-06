import axios from "axios";

// Change this to your computer's IP when testing on a real phone.
// Android Emulator: http://10.0.2.2:8000/api
// iOS Simulator: http://127.0.0.1:8000/api
// Physical phone: http://YOUR_PC_IP:8000/api

const api = axios.create({
  baseURL: "http://10.0.2.2:8000/api/",
});

export default api;