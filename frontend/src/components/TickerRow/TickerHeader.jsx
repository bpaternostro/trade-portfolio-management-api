import React from 'react'
import styles from './ticker-row.module.css'

const TickerHeader = () => {
  return (
    <div className={styles.tickerHeader}>
        <div>
            <span>
                Buy Information
            </span>
            <span>
                Ticker Current Data
            </span>
        </div>
        <div>   
              <span>
                
              </span>
              <span>
                
              </span>
              <span>
                #
              </span>
              <span>
                price
              </span>
              <span>
                fees
              </span>
              <span>
                total
              </span> 
              <span>
                date
              </span> 
              <span>
                price
              </span>
              <span>
                total
              </span>
              <span>
                diff $
              </span> 
              <span>
                diff %
              </span>
              <span>
                vol
              </span> 
              <span>
                % vol [-1]
              </span>
              <span>
                available
              </span>
              <span>
                trend
              </span>
              <span>
                index
              </span>
              <span>
                sell
              </span>
              <span>
                check sell
              </span>
        </div>
    </div>
  )
}

export default TickerHeader