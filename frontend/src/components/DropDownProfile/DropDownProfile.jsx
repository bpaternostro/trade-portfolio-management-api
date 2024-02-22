import React, { useEffect, useState, useRef } from 'react'
import  navbarStyle from '../Navbar/navbar.module.css'
import { useGlobalContext } from '../../context/GlobalContextProvider'

import buttonStyles from '../../style/buttons.module.css'

const DropDownProfile = () => {
    const {openProfile, setOpenProfile, portfolios, setSelectedTickers} = useGlobalContext()
    const {setActualPortfolio} = useGlobalContext()
    const menuRef = useRef()
    
    useEffect(() => {
        let handler = (e) => {
            if(!menuRef.current.contains(e.target)){
                setOpenProfile(false)
            }
        }
        
        document.addEventListener('mousedown', handler);

        return() =>{
            document.removeEventListener('mousedown', handler)
        }

    }, []);

    const handleClick = (e, portfolio) => {
        setActualPortfolio(portfolio)
        setSelectedTickers([])
        setOpenProfile(false)
    }

    return (
        <div ref={menuRef}>
            <ul className={`flex flex-col gap-4 ${ navbarStyle.dropDownProfile}`}>
                {portfolios && portfolios.map((p, index) => (<li key={index} onClick={(e) => handleClick(e, p)}>{p.name} </li>))}
            </ul>
        </div>
    )
}


export default DropDownProfile