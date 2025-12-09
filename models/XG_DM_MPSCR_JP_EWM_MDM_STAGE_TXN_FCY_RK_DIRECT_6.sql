WITH extract_ewm_ev_txn_v AS (
    SELECT
        SRC_DL,
        EV_ID,
        MSTR_SRC_STM_CD,
        MSTR_SRC_STM_KEY,
        VLD_FROM_TMS,
        VLD_TO_TMS,
        PRIM_AR_ID,
        TXN_BOOK_DT,
        TXN_CCY_AMT,
        TXN_CCY_CL_CD,
        TXN_RSN_TP_CL_CD,
        LDGR_CCY_AMT,
        LDGR_CCY_CL_CD
    FROM
        DM_MPSCR.EWM_EV_TXN_V
    WHERE
        SRC_DL = 'DL_DE'
        AND TXN_RSN_TP_CL_CD IN (
            'FEE_CMSN_PYMT', 'INT_PYMT', 'PNP_PYMT', 'PST_RSL_PYMT', 'TCNQL_PYMT', 'FNC_SVC_PYMT',
            'ADL_WRKOUT_COST', 'ADMIN_RCVR_COST', 'EXT_COST', 'FEE_CMSN_CHRG', 'INT_CHRG',
            'LGL_COST', 'LQD_COST', 'PST_RSL_COST', 'TCNQL_ADVNC_PYMT', 'PNP_ADVNC', 'FNC_SVC_CHRG',
            'WRT_OFF', 'FNC_CLM', 'AGRM_NET_SALE'
        )
        AND VLD_FROM_TMS <= TO_DATE('20240516000000', 'YYYYMMDDHH24MISS')
        AND TO_DATE('20240516000000', 'YYYYMMDDHH24MISS') < VLD_TO_TMS
),
extract_ewm_mdm_stage_transaction_fcy AS (
    SELECT
        SRC_DL,
        AR_ID AS PRIM_AR_ID,
        FCY_RK,
        DATA_DT
    FROM
        DM_MPSCR.EWM_MDM_STAGE_TRANSACTION_FCY
    WHERE
        DATA_DT = TO_DATE('20240516', 'YYYYMMDD')
        AND SRC_DL = 'DL_DE'
),
joined_data AS (
    SELECT
        e.SRC_DL,
        e.EV_ID,
        e.MSTR_SRC_STM_CD,
        e.MSTR_SRC_STM_KEY,
        e.VLD_FROM_TMS,
        e.VLD_TO_TMS,
        e.PRIM_AR_ID,
        e.TXN_BOOK_DT,
        e.TXN_CCY_AMT,
        e.TXN_CCY_CL_CD,
        e.TXN_RSN_TP_CL_CD,
        e.LDGR_CCY_AMT,
        e.LDGR_CCY_CL_CD,
        t.FCY_RK,
        t.DATA_DT
    FROM
        extract_ewm_ev_txn_v e
        INNER JOIN extract_ewm_mdm_stage_transaction_fcy t
        ON e.SRC_DL = t.SRC_DL AND e.PRIM_AR_ID = t.PRIM_AR_ID
),
deduplicated_data AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY SRC_DL, PRIM_AR_ID, FCY_RK, MSTR_SRC_STM_KEY ORDER BY SRC_DL) AS row_num
    FROM
        joined_data
),
final_data AS (
    SELECT
        SRC_DL,
        EV_ID,
        MSTR_SRC_STM_CD,
        MSTR_SRC_STM_KEY,
        VLD_FROM_TMS,
        VLD_TO_TMS,
        PRIM_AR_ID,
        TXN_BOOK_DT,
        TXN_CCY_AMT,
        TXN_CCY_CL_CD,
        TXN_RSN_TP_CL_CD,
        LDGR_CCY_AMT,
        LDGR_CCY_CL_CD,
        FCY_RK,
        current_timestamp() AS SYS_INRT_TMS,
        DATA_DT
    FROM
        deduplicated_data
    WHERE
        row_num = 1
)
SELECT
    *
FROM
    final_data;