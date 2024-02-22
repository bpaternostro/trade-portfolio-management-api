import React, { useEffect, useState } from 'react'
import { DropDownProfile } from '../'

import { FaPlusSquare } from "react-icons/fa";
import { FaEdit } from "react-icons/fa";

import { useGlobalContext } from '../../context/GlobalContextProvider'
import { useModalContext } from '../../context/ModalContextProvider'

import navbarStyle from './navbar.module.css'
import buttonStyle from '../../style/buttons.module.css'

const Navbar = () => {
    const {openProfile, setOpenProfile, actualPortfolio} = useGlobalContext()  
    const {setModalTitle, setModalText, toggleModal, setIsCreatePortfolioModal, setIsConfirmationModal, setIsEditModal, setIsIndicatorsModal, setIsEditPortfolioModal} = useModalContext()
    
    const handlePopUp = () => {
        setModalTitle("Create a new portfolio")
        setModalText(`Insert all the information`)
        setIsConfirmationModal(false)
        setIsEditModal(false)
        setIsIndicatorsModal(false)
        setIsCreatePortfolioModal(true)
        setIsEditPortfolioModal(false)
        toggleModal(true)
    }

    const handlePopUpEditPortfolio = () => {
        setModalTitle("Edit portfolio")
        setModalText(`Edit all the information`)
        setIsConfirmationModal(false)
        setIsEditModal(false)
        setIsIndicatorsModal(false)
        setIsCreatePortfolioModal(false)
        setIsEditPortfolioModal(true)
        toggleModal(true)
    }

    return (
        <header>    
            <h1>Portfolio management</h1>
            <nav>
                <div className={navbarStyle.profileMenu}>
                    <span className={navbarStyle.nickName} onClick={() => setOpenProfile(!openProfile)}><span role="img" aria-label="waving-hand">👋</span><span className={navbarStyle.username}>{localStorage.getItem('username')}</span></span>  
                    {openProfile && <DropDownProfile/>}  
                </div>
                <div className={navbarStyle.profileToolbar}>
                    <span>
                        <button onClick={handlePopUp} className={buttonStyle.iconButton}><FaPlusSquare size={20}/></button>
                        {actualPortfolio && <button onClick={handlePopUpEditPortfolio} className={buttonStyle.iconButton}><FaEdit size={20}/></button>}
                    </span>
                </div>
            </nav>
        </header>
    )
    }

export default Navbar