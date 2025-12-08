WITH remdup_rdu_highest_facility AS (
    SELECT
        *
    FROM
        V438S0P1
    QUALIFY
        ROW_NUMBER() OVER (PARTITION BY SRC_DL, AR_ID ORDER BY SRC_DL, AR_ID) = 1
),
join_jno_fcy_ar_lwst_hghst AS (
    SELECT
        *
    FROM
        V438S1P1
    LEFT OUTER JOIN V438S1P2 ON V438S1P1.SRC_DL = V438S1P2.SRC_DL AND V438S1P1.AR_ID = V438S1P2.AR_ID
),
transform_xfm_highest_facility AS (
    SELECT
        mov_AR_X_R_HIGHEST.HIGHEST_FCY_ID AS AR_ID,
        'Y' AS HIGHEST_FCY_IN_HRY
    FROM
        remdup_rdu_highest_facility AS mov_AR_X_R_HIGHEST
),
project_mov_mdm_fcy_all_cols AS (
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
            WHEN mov_FCY_AR_IDENTN.HIGHER_FCY_RK IS NULL THEN mov_FCY_AR_IDENTN.FCY_RK
            ELSE mov_FCY_AR_IDENTN.HIGHER_FCY_RK
        END AS HIGHER_FCY_RK,
        CASE
            WHEN mov_FCY_AR_IDENTN.HIGHEST_FCY_RK IS NULL THEN mov_FCY_AR_IDENTN.FCY_RK
            ELSE mov_FCY_AR_IDENTN.HIGHEST_FCY_RK
        END AS HIGHEST_FCY_RK,
        CASE
            WHEN mov_FCY_AR_IDENTN.HLEAF = 1 THEN 'Y'
            WHEN mov_FCY_AR_IDENTN.HLEAF = 0 THEN 'N'
            WHEN mov_FCY_AR_IDENTN.HIGHEST_FCY_IN_HRY = 'Y' THEN 'N'
            ELSE 'Y'
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
        transform_xfm_highest_facility AS mov_FCY_AR_IDENTN
)

SELECT
    DATA_DT,
    FCY_ID,
    SRC_STM_ID,
    DATE_FROM,
    AR_ID,
    DATE_TO,
    SRC_DL,
    FCY_RK,
    FCY_AR_TP,
    HIGHER_FCY_RK,
    HIGHEST_FCY_RK,
    LOWEST_LVL_IND,
    SPSDG_FCY_RK,
    COURT_CTRLD_WRKOUT_FILL_DT,
    COURT_CTRLD_WRKOUT_FCY,
    OUT_OF_COURT_WRKOUT_FCY,
    SPSDG_FCY_DT,
    COURT_CTRLD_WRKOUT_CLS_DT,
    CR_OBLG_DFLTD,
    FCY_VORTEX_ID,
    SYS_INRT_TMS
FROM
    project_mov_mdm_fcy_all_cols;