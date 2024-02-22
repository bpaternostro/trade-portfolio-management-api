import React, { useEffect, useState } from 'react'
import { useGlobalContext } from '../../context/GlobalContextProvider'
import TickerHeader from '../TickerRow/TickerHeader'
import TickerRow from '../TickerRow/TickerRow'
import TickerHeaderToolbar from '../TickerRow/TickerHeaderToolbar'

import Widget from '../Widget/Widget'
import style from './dashboard.module.css'
import indexStyle from '../../style/index.module.css'

const Dashboard = () => {
    const {actualPortfolio} = useGlobalContext()

    return (
        <div className={style.tableContainer}>
            {actualPortfolio && 
            <div className={style.table}>
                <div className={style.widgetContainer}>
                    <Widget name={"Portfolio Name"} value={actualPortfolio.name}></Widget>
                    <Widget name={"Start Value"} value={actualPortfolio.start_value}></Widget>
                    <Widget name={"Actual value"} value={actualPortfolio.actual_value}></Widget>
                    <Widget name={"Difference"} value={actualPortfolio.difference}></Widget>
                    <Widget name={"Performance"} value={actualPortfolio.performance}></Widget>
                    <Widget name={"Last Update"} value={actualPortfolio.last_update}></Widget>
                </div>
                <TickerHeader></TickerHeader>
                <TickerHeaderToolbar></TickerHeaderToolbar>
                {actualPortfolio.detail.map( (t, i) => (
                    <TickerRow tickerData={t} key={i}></TickerRow>
                ))}
            </div>}
        </div>
    )
}

export default Dashboard