import React, { useState, useEffect } from 'react'

import { useParams } from 'react-router-dom'

import { Dashboard, Sidebar, Navbar, Modal} from '../components'

import { API_ENDPOINTS } from '../apiConfig'
import { useGlobalContext } from '../context/GlobalContextProvider';
import { useModalContext } from '../context/ModalContextProvider';

import style from '../style/home.module.css'

import axios from 'axios'

const Home = () => {
  const trader = useParams()
  localStorage.setItem("operator", trader.id)
  const {actualPortfolio, setPortfolios, setActualPortfolio, portfolios, setLoading, loading, csrfToken, selectedTickers, setSelectedTickers } = useGlobalContext()
  const {toggleModal, toStatus} = useModalContext()
  const handleUpdateTicker = (e) => {
    e.preventDefault()
    let updatedStatus = selectedTickers.map((t) => ({ ...t, status: toStatus, portfolio: actualPortfolio.id, ticker: t.ticker.id}))
    axios.put(API_ENDPOINTS.portofoliosFinInstrumentUpdateStatus, updatedStatus, {headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
    }})
    .then((resp) => {
      setActualPortfolio(resp.data.portfolio_updated)
      setSelectedTickers([])
      let newListPortfolios = [...portfolios.filter(p => p.id !== resp.data.portfolio_updated.id), resp.data.portfolio_updated]
      setPortfolios([...newListPortfolios].sort((a, b) => a.name.localeCompare(b.name)))
      return
    })
    .catch((err) => {
        console.log(err)
    })
    .finally(() => {
      toggleModal()
    })
  }

  useEffect(() => {
    setLoading(!loading)
    fetch(API_ENDPOINTS.trader + `/${localStorage.getItem("operator")}`, {
      mode: 'cors',
      method: 'get',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
      }
    })
    .then( res => {
      if(!res.ok){
        throw new Error('X');
      }
      return res.json()
    })
    .then( data => {
      setPortfolios(data.portfolios)
      setActualPortfolio(portfolios.find((p) => p.id == actualPortfolio.id))
      localStorage.setItem("username", data.name)
    })
    .finally(() => {
      setLoading(!loading)
    })
  },[])

  return (
    <main>
      {portfolios && <Navbar></Navbar> }
      <div>
        {portfolios && <Dashboard></Dashboard> }
      </div>
      <Sidebar></Sidebar>   
      <Modal onConfirm={handleUpdateTicker}></Modal>
       
    </main>
    
  )
}

export default Home