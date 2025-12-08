WITH
-- CTE for the join operation
JNO_FCY_AR_LWST_HGHST AS (
    SELECT
        t1.*,
        t2.*
    FROM
        V438S1P1 t1
        LEFT OUTER JOIN V438S1P2 t2
        ON t1.SRC_DL = t2.SRC_DL AND t1.AR_ID = t2.AR_ID
),

-- CTE for the remove duplicates operation
RDU_Highest_Facility AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY SRC_DL, AR_ID ORDER BY SRC_DL, AR_ID) AS row_num
    FROM
        JNO_FCY_AR_LWST_HGHST
    QUALIFY row_num = 1
),

-- CTE for the transformation operation
XFM_HIGHEST_FACILITY AS (
    SELECT
        mov_AR_X_R_HIGHEST.HIGHEST_FCY_ID AS AR_ID,
        'Y' AS HIGHEST_FCY_IN_HRY
    FROM
        RDU_Highest_Facility mov_AR_X_R_HIGHEST
),

-- CTE for the sort operation
SRT_AR_X_R_HIGHEST AS (
    SELECT
        *
    FROM
        XFM_HIGHEST_FACILITY
    ORDER BY
        SRC_DL ASC,
        AR_ID ASC
)

-- Final SELECT statement
SELECT
    DATA_DT,
    OBJ_AR_ID AS FCY_ID,
    MSTR_SRC_STM_CD AS SRC_STM_ID,
    mov_FCY_AR_IDENTN.SYS_VLD_FROM_TMS AS DATE_FROM,
    AR_ID,
    VLD_TO_TMS AS DATE_TO,
    SRC_DL,
    FCY_RK,
    FCY_AR_TP,
    CASE
        WHEN IsNull(mov_FCY_AR_IDENTN.HIGHER_FCY_RK) THEN mov_FCY_AR_IDENTN.FCY_RK
        ELSE mov_FCY_AR_IDENTN.HIGHER_FCY_RK
    END AS HIGHER_FCY_RK,
    CASE
        WHEN IsNull(mov_FCY_AR_IDENTN.HIGHEST_FCY_RK) THEN mov_FCY_AR_IDENTN.FCY_RK
        ELSE mov_FCY_AR_IDENTN.HIGHEST_FCY_RK
    END AS HIGHEST_FCY_RK,
    CASE
        WHEN mov_FCY_AR_IDENTN.HLEAF = 1 THEN 'Y'
        WHEN mov_FCY_AR_IDENTN.HLEAF = 0 THEN 'N'
        ELSE
            CASE
                WHEN mov_FCY_AR_IDENTN.HIGHEST_FCY_IN_HRY = 'Y' THEN 'N'
                ELSE 'Y'
            END
    END AS LOWEST_LVL_IND,
    FCY_RK AS SPSDG_FCY_RK,
    COURT_CTRLD_WRKOUT_FILL_DT,
    COURT_CTRLD_WRKOUT_FCY,
    OUT_OF_COURT_WRKOUT_FCY,
    mov_FCY_AR_IDENTN.SPSDG_FCY_DT AS SPSDG_FCY_DT,
    COURT_CTRLD_WRKOUT_CLS_DT,
    CR_OBLG_DFLTD,
    mov_FCY_AR_IDENTN.AR_IDENTN_NM AS FCY_VORTEX_ID,
    CURRENT_TIMESTAMP() AS SYS_INRT_TMS
FROM
    SRT_AR_X_R_HIGHEST