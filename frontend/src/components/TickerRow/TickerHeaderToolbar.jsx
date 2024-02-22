import React from 'react'
import styles from './ticker-row.module.css'

import buttonStyle from '../../style/buttons.module.css'

import { FaPlusSquare } from "react-icons/fa";
import { FaShareFromSquare } from "react-icons/fa6";
import { FaRegStopCircle } from "react-icons/fa";
import { MdOutlineDelete } from "react-icons/md";

import { useModalContext } from '../../context/ModalContextProvider'
import { useGlobalContext } from '../../context/GlobalContextProvider';

const TickerHeaderToolbar = () => {
  const {setModalTitle, setModalText, toggleModal, setToStatus, setIsEditModal, setIsSellTickerModal, setIsIndicatorsModal, setIsSellBookModal, setIsConfirmationModal, setIsCreatePortfolioModal, setIsEditPortfolioModal, setIsMoveModal} = useModalContext()
  const {setActualTicker} = useGlobalContext()
    
  const handlePopUp = () => {
    setActualTicker(null)
    setIsEditModal(true)
    setIsIndicatorsModal(false)
    setIsConfirmationModal(false)
    setIsCreatePortfolioModal(false)
    setIsEditPortfolioModal(false)
    setIsSellTickerModal(false)
    setIsSellBookModal(false)
    setModalTitle("Agregar Ticker al portfolio")
    setModalText(`Agrega el ticker cabron`)
    toggleModal(true)
  }

  const handlePopUpDelete = () => {
    setIsConfirmationModal(true)
    setIsEditModal(false)
    setIsIndicatorsModal(false)
    setIsCreatePortfolioModal(false)
    setIsEditPortfolioModal(false)
    setIsMoveModal(false)
    setIsSellTickerModal(false)
    setIsSellBookModal(false)
    setModalTitle("Ticker deletion from portfolio")
    setModalText("Are you sure you want to delete this ticker?")
    toggleModal()
    setToStatus(4)
  }

  const handlePopUpStop = () => {
    setIsConfirmationModal(true)
    setIsEditModal(false)
    setIsIndicatorsModal(false)
    setIsMoveModal(false)
    setIsSellTickerModal(false)
    setIsSellBookModal(false)
    setModalTitle("Stop Ticker in portfolio")
    setModalText("Are you sure you want to stop this ticker?")
    toggleModal()
    setToStatus(1)      
  }

  const handlePopUpMove = () => {
    setIsConfirmationModal(false)
    setIsEditModal(false)
    setIsIndicatorsModal(false)
    setIsSellTickerModal(false)
    setIsMoveModal(true)
    setIsSellBookModal(false)
    setModalTitle("Move Ticker to portfolio")
    setModalText("Are you sure you want to move this ticker?")
    toggleModal()
  }

  return (
    <div className={styles.tickerHeaderToolbar}>
        <div>
          <span className={styles.toolBar}>
              <button onClick={handlePopUp} className={buttonStyle.iconButton}><FaPlusSquare size={18} title="Add ticker"/></button>
              <button className={buttonStyle.iconButton} onClick={(e) =>  handlePopUpMove(e)}><FaShareFromSquare size={18} title="Move ticker"/></button>
              <button className={buttonStyle.iconButton} onClick={(e) =>  handlePopUpStop(e)} ><FaRegStopCircle size={18} color={"#FFF"} title="Stop ticker"/></button>
              <button className={buttonStyle.iconButton} onClick={(e) =>  handlePopUpDelete(e)}><MdOutlineDelete size={18} color={"#FFF"} title="Delete ticker"/></button>
          </span>
        </div>
    </div>
  )
}

export default TickerHeaderToolbar