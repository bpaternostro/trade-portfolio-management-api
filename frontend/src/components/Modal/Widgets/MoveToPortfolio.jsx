import { React, useState, useEffect } from 'react'


import { useGlobalContext } from '../../../context/GlobalContextProvider'
import { useModalContext } from '../../../context/ModalContextProvider'

import  modalStyle from '../modal.module.css'
import  buttonStyle from '../../../style/buttons.module.css'

import { API_ENDPOINTS } from '../../../apiConfig'
import axios from 'axios'

const MoveToPortfolio = () => {
    const {actualPortfolio, csrfToken, portfolios, selectedTickers, setActualPortfolio, setSelectedTickers, setPortfolios} = useGlobalContext()
    const {toggleModal} = useModalContext()
    const initialValues = {
        portfolio_from: actualPortfolio.id,
        portfolio_to: 1,
    }
    const [formValues, setFormValues] = useState(initialValues)
    
    const handleChangeInput = (value, name) => {
        if(value === ""){
            value = 0
        }
        const aux = {...formValues, [name]:value}
        setFormValues(aux)
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        let newPortfolio = selectedTickers.map((t) => ({ ...t, old_portfolio:actualPortfolio.id, portfolio: formValues.portfolio_to, ticker: t.ticker.id}))
        axios.put(API_ENDPOINTS.portofoliosFinInstrumentMoveTicker, newPortfolio, {headers: {
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

  return (
    <div className={modalStyle.formContainer}>
        <form onSubmit={(e) => handleSubmit(e)}>
            <div className={modalStyle.formBody}>
                <input style={{display:"none"}} type="text" name="portfolio_from" value={formValues.portfolio} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>
                <span>
                    <label htmlFor="portfolio_to">Por</label>
                    <select name="portfolio_to" onChange={(e) => handleChangeInput(e.target.value, e.target.name)}>
                        {portfolios.map((p, i) => <option key={i} value={p.id}>{p.name}</option>)}
                    </select>
                </span>
            </div>
            <div className={modalStyle.formFooter}>
                <button type="submit" className={buttonStyle.buttonPrimary}>Move</button>
                <button className={`${ buttonStyle.buttonPrimary } ${modalStyle.acceptModal}`} onClick={toggleModal}>Cancel</button>
            </div>
        </form>
    </div>
  )
}

export default MoveToPortfolio