import { React, useState, useEffect } from 'react'


import { useGlobalContext } from '../../../context/GlobalContextProvider'
import { useModalContext } from '../../../context/ModalContextProvider'

import  modalStyle from '../modal.module.css'
import  buttonStyle from '../../../style/buttons.module.css'

import { API_ENDPOINTS } from '../../../apiConfig'

const EditTicker = () => {
    const {actualPortfolio, setActualPortfolio, actualTicker, setActualTicker, tickers, csrfToken} = useGlobalContext()
    const {setModalError, toggleModal} = useModalContext()
    let today = new Date()
    const initialValues = {
        portfolio: 0,
        ticker: 1,
        status: 0,
        buy_quantity: 0,
        buy_price: 0,
        buy_date: today.toISOString().split('T')[0]
    }
    const [formValues, setFormValues] = useState(initialValues)
    
    const handleChangeInput = (value, name) => {
        if(value === ""){
            value = 0
        }
        const aux = {...formValues, [name]:value}
        setFormValues(aux)
    }

    const handleChangeInputDate = (value, name) => {
        if(value === ""){
            value = null
        }
        const aux = {...formValues, [name]:value}
        setFormValues(aux)
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        formValues.portfolio = actualPortfolio.id
        let method = actualTicker ? "PUT": "POST" 
        fetch(actualTicker ? `${API_ENDPOINTS.portofoliosFinInstrument}/${actualTicker.id}/`: `${API_ENDPOINTS.portofoliosFinInstrument}/`, 
        {
            method: method,
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify(formValues)
        })
        .then( resp => {
            return resp.json()
        })
        .then( data => {
            toggleModal()
            setActualPortfolio(data.portfolio_updated)
            return
        })
        .catch(error => {
            console.log(error)
            setModalError(error)
            return
        })
        .finally(() => {
            setActualTicker(false)
        })
    }

    useEffect(() => {
        if(actualTicker){
            setFormValues({
                portfolio: actualPortfolio.id || 1,
                ticker: actualTicker.ticker,
                status: actualTicker.status || 0,
                buy_quantity: actualTicker.buy_quantity,
                buy_price: actualTicker.buy_price,
                buy_date: actualTicker.buy_date,
            })
        }else{
            setFormValues(initialValues)
        }
        
    },[actualTicker])

  return (
    <div className={modalStyle.formContainer}>
        <form onSubmit={(e) => handleSubmit(e)}>
            <div className={modalStyle.formBody}>
                <input style={{display:"none"}} type="text" name="portfolio" value={formValues.portfolio} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>
                <span>
                    <label htmlFor="ticker">Ticker</label>
                    {
                        actualTicker ? 
                        <input type="text" name="ticker" value={formValues.ticker.symbol} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>
                        :
                        <select name="ticker" onChange={(e) => handleChangeInput(e.target.value, e.target.name)}>
                            {tickers.map((t, i) => <option key={i} value={t.id}>{t.symbol}</option>)}
                        </select>
                    }
                </span>
                <span>
                    <label htmlFor="buy_quantity">Buy #</label>
                    <input type="number" name="buy_quantity" value={formValues.buy_quantity} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>    
                </span>
                <span>
                    <label htmlFor="buy_price">Buy price</label>
                    <input type="number" name="buy_price" value={formValues.buy_price} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>    
                </span>
                <span>
                    <label htmlFor="buy_date">Buy date</label>
                    <input type="date" name="buy_date" value={formValues.buy_date} onChange={(e) => handleChangeInputDate(e.target.value, e.target.name)}/>    
                </span>
            </div>
            <div className={modalStyle.formFooter}>
                <button type="submit" className={buttonStyle.buttonPrimary}>{actualTicker ? 'Save': 'Create'}</button>
                <button className={`${ buttonStyle.buttonPrimary } ${modalStyle.acceptModal}`} onClick={toggleModal}>Cancel</button>
            </div>
        </form>
    </div>
  )
}

export default EditTicker