import React from 'react'
import { Route, Routes } from 'react-router-dom'
import { Home } from '../pages'
import { ROOT } from '../apiConfig'
import { API_ENDPOINTS } from '../apiConfig'
const PageRouter = () => {
  const queryParameters = new URLSearchParams(window.location.search)
  localStorage.setItem("operator", queryParameters.get("operator"))
  return (
    <>
      <Routes>
          <Route path={ROOT} element={<Home/>} />
      </Routes>
    </>
  )
}

export default PageRouter