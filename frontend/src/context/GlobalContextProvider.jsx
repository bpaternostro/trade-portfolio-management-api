import React, { useContext, createContext, useState, useEffect } from 'react'

import { getCookie } from '../helpers/CoreMethods';
import { API_ENDPOINTS } from '../apiConfig';

import axios from 'axios'


const GlobalContext = createContext()
const GlobalContextProvider = ({children}) => {
    const [portfolios, setPortfolios] = useState([])
    const [actualPortfolio, setActualPortfolio] = useState(null)
    const [openProfile, setOpenProfile] = useState(false)
    const [showSidebar, setShowSidebar] = useState(false)
    const [actualTicker, setActualTicker] = useState(false)
    const [tickerHasChanged, setTickerHasChanged] = useState(false)
    const [portfolioHasChanged, setPortfolioHasChanged] = useState(false)
    const [tickers, setTickers] = useState([])
    const [portfolioTypes, setPortfolioTypes] = useState([])
    const [portfolioStatus, setPortfolioStatus] = useState([])
    const [loading, setLoading] = useState(true)
    const [selectedTickers, setSelectedTickers] = useState([])
    const csrfToken = getCookie('csrftoken');

    useEffect(() => {
        axios.get(API_ENDPOINTS.financialInstruments)
        .then(res =>{
            setTickers(res.data)
        })

        axios.get(API_ENDPOINTS.list)
        .then(res =>{
            setPortfolioTypes(res.data.portfolio_types)
            setPortfolioStatus(res.data.status)
        })

    },[])

    return (
        <GlobalContext.Provider value={{
            actualPortfolio, setActualPortfolio,
            openProfile, setOpenProfile,
            csrfToken,
            showSidebar, setShowSidebar,
            actualTicker, setActualTicker,
            tickerHasChanged, setTickerHasChanged,
            portfolioTypes, portfolioStatus,
            portfolios, setPortfolios,
            portfolioHasChanged, setPortfolioHasChanged,
            loading, setLoading,
            selectedTickers, setSelectedTickers,
            tickers
            }}>
            {children}
        </GlobalContext.Provider>
    )
}

/*cremos un custom Hook para utilizar el contexto */
export const useGlobalContext = () => useContext(GlobalContext)

export default GlobalContextProvider