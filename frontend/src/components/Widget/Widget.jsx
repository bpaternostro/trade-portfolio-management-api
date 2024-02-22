import React from 'react'

import style from "./widget.module.css"

const Widget = ({name, value}) => {
  return (
    <div className={style.widget}>
        <h3 className={style.widgetTitle}>{name}</h3>
        <span className={style.widgetValue}>{value}</span>
    </div>
  )
}

export default Widget