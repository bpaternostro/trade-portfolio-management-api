import React from 'react'
import { Route, Routes } from 'react-router-dom'
import { Home } from '../pages'
import { ROOT } from '../apiConfig'
import { API_ENDPOINTS } from '../apiConfig'
const PageRouter = () => {
  return (
    <>
      <Routes>
          <Route path={`${ROOT}/:id`} element={<Home/>} />
      </Routes>
    </>
  )
}

export default PageRouter