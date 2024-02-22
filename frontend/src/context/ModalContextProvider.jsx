import React, { useContext, createContext, useState } from 'react'

const ModalGlobalContext = createContext()
const ModalContextProvider = ({children}) => {
    const [modal, setModal] = useState(false)
    const [modalOk, setModalOk] = useState(false)
    const [modalTitle, setModalTitle] = useState(false)
    const [modalText, setModalText] = useState(false)
    const [modalError, setModalError] = useState(false)
    const [entityId, setEntityId] = useState("")
    const [errorMsg, setErrorMsg] = useState("")
    const [toStatus, setToStatus] = useState()
    const [onClose, setOnClose] = useState()
    const [isIndicatorsModal, setIsIndicatorsModal] = useState(false)
    const [isEditModal, setIsEditModal] = useState(false)
    const [isCreatePortfolioModal, setIsCreatePortfolioModal] = useState(false)
    const [isEditPortfolioModal, setIsEditPortfolioModal] = useState(false)
    const [isConfirmationModal, setIsConfirmationModal] = useState(false)
    const [isMoveModal, setIsMoveModal] = useState(false)
    const [isSellTickerModal, setIsSellTickerModal] = useState(false)
    const [isSellBookModal,setIsSellBookModal] = useState(false)

    const toggleModal = () => {
        setModal(!modal)
    }

    return (
        <ModalGlobalContext.Provider value={{
            modal,
            toggleModal,
            modalOk, setModalOk,
            modalTitle, setModalTitle,
            modalText, setModalText,
            modalError, setModalError,
            entityId, setEntityId,
            toStatus, setToStatus,
            onClose, setOnClose,
            isIndicatorsModal, setIsIndicatorsModal,
            isEditModal, setIsEditModal,
            isCreatePortfolioModal, setIsCreatePortfolioModal,
            isConfirmationModal, setIsConfirmationModal,
            isEditPortfolioModal, setIsEditPortfolioModal,
            isMoveModal, setIsMoveModal,
            isSellTickerModal, setIsSellTickerModal,
            isSellBookModal,setIsSellBookModal,
            setErrorMsg
            }}>
            {children}
        </ModalGlobalContext.Provider>
    )
}

/*cremos un custom Hook para utilizar el contexto */
export const useModalContext = () => useContext(ModalGlobalContext)

export default ModalContextProvider