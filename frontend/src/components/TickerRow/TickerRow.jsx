import React, {useEffect, useState} from 'react'

import { Link } from 'react-router-dom'
import styles from './ticker-row.module.css'
import indexStyles from '../../style/index.module.css'
import buttonStyles from '../../style/buttons.module.css'

import { VscDashboard } from "react-icons/vsc";
import { BsArrowUpRightSquareFill, BsArrowDownRightSquareFill } from "react-icons/bs";
import { GrTransaction } from "react-icons/gr";
import { FaMoneyCheck } from "react-icons/fa";


import {API_ENDPOINTS, ROOT} from '../../apiConfig'
import { useGlobalContext } from '../../context/GlobalContextProvider';
import { useModalContext } from '../../context/ModalContextProvider'

import axios from 'axios'

const TickerRow = ({tickerData}) => {
    const {
        id,  
        ticker,
        status,
        current_price,
        buy_quantity,
        buy_price_str,
        buy_date,
        current_total,
        variation,
        variation_in_usd,
        buy_fees,
        total_buy,
        available,
        can_sell,
        volume,
        volume_diff
       } = tickerData || {}
    const {actualPortfolio, setActualTicker,selectedTickers, setSelectedTickers} = useGlobalContext();
    const {setModalTitle, 
          setModalText, 
          toggleModal, 
          setIsIndicatorsModal, 
          setIsEditModal, 
          setIsCreatePortfolioModal, 
          setIsConfirmationModal, 
          setIsEditPortfolioModal,
          setIsSellBookModal,
          setIsSellTickerModal} = useModalContext()
    const [selected, setSelected] = useState(false)

    const handlePopUpIndicators = (e) => {
      setModalTitle("Ticker indicators")
      setModalText(`Show ticker indicators`)
      setIsIndicatorsModal(true)
      setIsEditModal(false)
      setIsConfirmationModal(false)
      setIsCreatePortfolioModal(false)
      setIsEditPortfolioModal(false)
      setIsSellTickerModal(false)
      setIsSellBookModal(false)
      setActualTicker(tickerData)
      toggleModal()
    }

    const handlePopUpSell = (e) => {
      setModalTitle("Sell Ticker")
      setModalText(`Sell ticker`)
      setIsIndicatorsModal(false)
      setIsEditModal(false)
      setIsConfirmationModal(false)
      setIsCreatePortfolioModal(false)
      setIsEditPortfolioModal(false)
      setIsSellTickerModal(true)
      setIsSellBookModal(false)
      setActualTicker(tickerData)
      toggleModal()
    }

    const handlePopUpSellBook = (e) => {
      setModalTitle(`Sell book for ${tickerData.ticker.symbol}`)
      setModalText(`Sell Book Detail`)
      setIsIndicatorsModal(false)
      setIsEditModal(false)
      setIsConfirmationModal(false)
      setIsCreatePortfolioModal(false)
      setIsEditPortfolioModal(false)
      setIsSellTickerModal(false)
      setIsSellBookModal(true)
      setActualTicker(tickerData)
      toggleModal()
    }

    const handlePopUpEdit = (e) => {
      if(e.target.tagName !== "SPAN" && e.target.tagName !== "DIV" ){
        return
      }
      setModalTitle("Edit Ticker in portfolio")
      setModalText(`Edit ticker in portfolio`)
      setIsEditModal(true)
      setIsIndicatorsModal(false)
      setIsConfirmationModal(false)
      setIsCreatePortfolioModal(false)
      setIsEditPortfolioModal(false)
      setIsSellTickerModal(false)
      setIsSellBookModal(false)
      setActualTicker(tickerData)
      toggleModal()
    }

    const handleCheckboxChange = (e) => {
      setSelected(!selected)
      return
    }

    useEffect(() => {
      setSelectedTickers(selected ? [...selectedTickers, tickerData] : selectedTickers.filter(t => t.id !== tickerData.id))
    },[selected])


    useEffect(() => {
      console.log("vino")
      setSelectedTickers([])
      setSelected(false)
    },[actualPortfolio])

    const globalStatus = 1
    return (
        <div className={styles.tickerRow}>
            <div onClick={(e) =>  handlePopUpEdit(e)}>
                <span>
                  <input className={styles.tickerLabelCheck} type="checkbox" onChange={(e) => handleCheckboxChange(e)} value={selected} />
                </span>
                <span className={styles.tickerLabelContainer}>
                  <span className={styles.tickerLabel} style={{background: status ? "#C70039": "#3ED17A"}}></span>
                  {ticker.symbol}
                </span>
                <span>
                  <span className={styles.mobileLabel}># buy</span>
                  {buy_quantity}
                </span>
                <span>
                  <span className={styles.mobileLabel}>$ buy</span>
                  {buy_price_str}
                </span>
                <span>
                  <span className={styles.mobileLabel}>buy fees</span>
                  {buy_fees}
                </span>
                <span>
                  <span className={styles.mobileLabel}>total buy</span>
                  {total_buy}
                </span>
                <span className={styles.tickerDate}>
                  <span className={styles.mobileLabel}>buy date</span>
                  {buy_date}
                </span>
                <span>
                  <span className={styles.mobileLabel}>current $</span>
                  {current_price}
                </span>
                <span>
                  <span className={styles.mobileLabel}>current total</span>
                  {current_total}
                </span>
                <span>
                  <span className={styles.mobileLabel}>var $</span>
                  {variation_in_usd}
                </span>
                <span>
                  <span className={styles.mobileLabel}>var</span>
                  {variation}
                </span>
                <span>
                  <span className={styles.mobileLabel}>vol</span>
                  {volume}
                </span>
                <span>
                  <span className={styles.mobileLabel}>vol diff</span>
                  {volume_diff}
                </span>
                <span>
                  <span className={styles.mobileLabel}>available</span>
                  {available}
                </span>
                <span>
                  <span className={styles.mobileLabel}>status</span>
                  {globalStatus ? <BsArrowUpRightSquareFill size={18} color={"#3ED17A"}/>:<BsArrowDownRightSquareFill size={20} color={"#C70039"}/>} 
                </span>
                <span>
                  <button className={buttonStyles.iconButton} onClick={(e) =>   handlePopUpIndicators(e)}><VscDashboard size={18} color={"#FFF"} title="Check indicators"/></button>
                </span>
                <span>
                  {can_sell ? <button className={buttonStyles.iconButton} onClick={(e) =>   handlePopUpSell(e)}><GrTransaction size={18} color={"#FFF"} title="Sell Ticker"/></button>: <span>Sold out</span>}
                </span>
                <span>
                  <button className={buttonStyles.iconButton} onClick={(e) =>   handlePopUpSellBook(e)}><FaMoneyCheck size={18} color={"#FFF"} title="Check Sells"/></button>
                </span>
            </div>
        </div>
    )
}

export default TickerRow