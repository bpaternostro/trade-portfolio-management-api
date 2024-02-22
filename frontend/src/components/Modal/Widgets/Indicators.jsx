import React from 'react'

import modalStyle from '../modal.module.css'
import buttonStyle from '../../../style/buttons.module.css'
import { useModalContext } from '../../../context/ModalContextProvider'

const Indicators = () => {
  const {toggleModal} = useModalContext()
  return (
    <div className={modalStyle.formContainer}>
      <div className={modalStyle.formBody}>
        <div>
          <span>RSI</span><span>1</span><span>OK</span>
        </div>
        <div>
          <span>Bollinger</span><span>1</span><span>OK</span>
        </div>
        <div>
          <span>Trending line</span><span>1</span><span>OK</span>
        </div>
      </div>
      <div className={modalStyle.formFooter}>
          <button className={`${ buttonStyle.buttonPrimary } ${modalStyle.acceptModal}`} onClick={toggleModal}>Close</button>
      </div>
    </div>
  )
}

export default Indicators