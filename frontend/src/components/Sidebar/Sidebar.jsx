import React, { useEffect, useState } from 'react'

import styles from './sidebar.module.css'
import buttonStyles from '../../style/buttons.module.css'
import indexStyle  from '../../style/index.module.css'
import { IoIosCloseCircle } from "react-icons/io";
import { useGlobalContext } from '../../context/GlobalContextProvider'

const Sidebar = () => {
  const {showSidebar, setShowSidebar} = useGlobalContext()


  return (
    <div style={{display: showSidebar ? "block": "none"}} className={styles.container}>
      <div className={styles.headerBar}>
        <button className={buttonStyles.iconButton} onClick={() => setShowSidebar(false)}><IoIosCloseCircle size={20}/></button>
      </div>
    </div>
  )
}

export default Sidebar