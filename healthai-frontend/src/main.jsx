import React from "react";
import { AuthProvider } from "./context/AuthContext";
import ReactDOM from "react-dom/client";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import "bootstrap-icons/font/bootstrap-icons.css";
import "./styles/page.css";

import "./styles/global.css";

import App from "./App";

ReactDOM.createRoot(document.getElementById("root")).render(
  
  <AuthProvider>

    <App />

  </AuthProvider>
);