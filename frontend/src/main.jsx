import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import { BrowserRouter } from 'react-router-dom'
import GlobalContextProvider from './context/GlobalContextProvider.jsx'
import ModalContextProvider from './context/ModalContextProvider.jsx'
import ScrollToTop from "./helpers/ScrollToTop";

ReactDOM.createRoot(document.getElementById('root')).render(
    <GlobalContextProvider>
        <ModalContextProvider>
            <BrowserRouter>
                <ScrollToTop />
                <App />
            </BrowserRouter>
        </ModalContextProvider>
    </GlobalContextProvider>
)