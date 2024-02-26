import { React, useState, useEffect } from 'react'


import { useGlobalContext } from '../../../context/GlobalContextProvider'
import { useModalContext } from '../../../context/ModalContextProvider'

import  modalStyle from '../modal.module.css'
import  buttonStyle from '../../../style/buttons.module.css'

import { API_ENDPOINTS } from '../../../apiConfig'

const SellTicker = () => {
    const {setActualPortfolio, actualTicker, setActualTicker, csrfToken} = useGlobalContext()
    const {setModalError, toggleModal} = useModalContext()
    const [error, setError] = useState(false)

    let today = new Date()
    const initialValues = {
        portofolio_financial_instrument: 0,
        sell_quantity: 0,
        sell_price: 0,
        sell_date: today.toISOString().split('T')[0]
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
        if(formValues.sell_quantity > actualTicker.available){
            setError(`It is not possible to sell more than ${actualTicker.available}`)
            return 
        }
        fetch(`${API_ENDPOINTS.portofoliosFinInstrumentOperation}/`, 
        {
            method: "POST",
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
                portofolio_financial_instrument: actualTicker.id,
                sell_quantity: actualTicker.sell_quantity ? actualTicker.sell_quantity: 0,
                sell_price: actualTicker.sell_price ? actualTicker.sell_price: 0,
                sell_date: today.toISOString().split('T')[0]
            })
        }else{
            setFormValues(initialValues)
        }
        
    },[actualTicker])

  return (
    <div className={modalStyle.formContainer}>
        <form onSubmit={(e) => handleSubmit(e)}>
            <div className={modalStyle.formBody}>
                <span>
                    <label htmlFor="sell_quantity">Sell #</label>
                    <input type="number" name="sell_quantity" value={formValues.sell_quantity} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>    
                </span>
                <span>
                    <label htmlFor="sell_price">Sell price</label>
                    <input type="number" name="sell_price" value={formValues.sell_price} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>    
                </span>
                <span>
                    <label htmlFor="sell_date">Sell date</label>
                    <input type="date" name="sell_date" value={formValues.sell_date} onChange={(e) => handleChangeInputDate(e.target.value, e.target.name)}/>        
                </span>
                { error && <span className={modalStyle.errorMessage}>{error}</span>}
            </div>
            <div className={modalStyle.formFooter}>
                <button type="submit" className={buttonStyle.buttonPrimary}>{actualTicker ? 'Save': 'Create'}</button>
                <button className={`${ buttonStyle.buttonPrimary } ${modalStyle.acceptModal}`} onClick={toggleModal}>Cancel</button>
            </div>
        </form>
    </div>
  )
}

export default SellTicker