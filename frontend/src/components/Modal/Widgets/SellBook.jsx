import React, { useEffect, useState } from 'react'

import modalStyle from '../modal.module.css'
import buttonStyle from '../../../style/buttons.module.css'

import axios from 'axios'
import { API_ENDPOINTS } from '../../../apiConfig'

import { useGlobalContext } from '../../../context/GlobalContextProvider'
import { useModalContext } from '../../../context/ModalContextProvider'

const SellBook = () => {
  const {actualTicker, csrfToken} = useGlobalContext();
  const {toggleModal} = useModalContext()
  const [tickerList, setTickerList] = useState([])
  
  useEffect(() => {
    axios.get(`${API_ENDPOINTS.portofoliosFinInstrument}/${actualTicker.id}/get-sell/`, {}, {headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
    }})
    .then((resp) => {
      setTickerList(resp.data)
    })
    .catch((error) => {
      console.log(error)
    })
  }, [])
  
  return (
    <div className={modalStyle.formContainer}>
      <div className={modalStyle.formBody}>
        <div className={modalStyle.sellTable}>
          <div className={modalStyle.sellTableHeader}><span># Sell</span><span>$</span><span>Sell date</span></div>
          {
            tickerList && tickerList.length ? tickerList.map((i, t) =><div key={i} className={modalStyle.sellRow}><span>{t.sell_quantity}</span><span>{t.sell_price}</span><span>{t.sell_date}</span></div>)
            :
            <span>There is no sells for this ticker</span> 
          }
        </div>
      </div>
      <div className={modalStyle.formFooter}>
          <button className={`${ buttonStyle.buttonPrimary } ${modalStyle.acceptModal}`} onClick={toggleModal}>Close</button>
      </div>
    </div>
  )
}

export default SellBook