
import React, { useEffect, useState } from 'react'

import  modalStyle from './modal.module.css'
import  buttonStyle from '../../style/buttons.module.css'

import { useGlobalContext } from '../../context/GlobalContextProvider'
import { useModalContext } from '../../context/ModalContextProvider'

import {Indicators, EditTicker, CreatePortfolio, MoveToPortfolio, SellTicker, SellBook} from '../index'

import axios from 'axios'

const Modal = ({onConfirm}) => {
    const {modalTitle, 
        modalText, 
        modal, 
        toggleModal, 
        onClose, 
        isIndicatorsModal, 
        isEditModal, 
        isCreatePortfolioModal, 
        isEditPortfolioModal,
        isConfirmationModal,
        isMoveModal,
        isSellTickerModal,
        isSellBookModal} = useModalContext()

    if(modal){
        document.body.classList.add('active-modl')
    }else{
        document.body.classList.remove('active-modl')
    }

    return (
        <>  
        {   
            modal && (
            

            <div className={ modalStyle.modal }>
                <div className={ modalStyle.overlay }>
                    <button className={modalStyle.closeModal} onClick={toggleModal}>X</button>
                </div>
                <div className={modalStyle.modalContent}>
                    <h2>{modalTitle}</h2>
                    {isConfirmationModal ?
                        <div>
                            <h3>{modalText}</h3>
                        </div>
                    : 
                        <div>
                            {isIndicatorsModal && <Indicators/> }
                            {isEditModal && <EditTicker/> }
                            {isCreatePortfolioModal && <CreatePortfolio/> }
                            {isEditPortfolioModal && <CreatePortfolio/> }
                            {isMoveModal && <MoveToPortfolio/> }
                            {isSellTickerModal && <SellTicker/> }
                            {isSellBookModal && <SellBook/> }
                        </div> 
                    }
                    <div className={modalStyle.modalFooter}>
                        {isConfirmationModal ? 
                            <span>
                                <button className={`${ buttonStyle.buttonPrimary } ${modalStyle.acceptModal}`} onClick={(e) => onConfirm(e)}>Confirm</button>
                                <button className={`${ buttonStyle.buttonPrimary } ${modalStyle.acceptModal}`} onClick={toggleModal}>Cancel</button>
                            </span>
                            :
                            <span></span> 
                        }
                    </div>
                </div>  
            </div>)
        }
            
        </>
    )
}

export default Modal