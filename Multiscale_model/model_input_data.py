"""
Приблизительные исходные данные для многомасштабной модели
воздействия ИИ на общество и экономику.

Единицы:
- ВРП: млрд руб. в год;
- выручка, затраты, инвестиции: млн руб. в год;
- ставки: руб./час;
- вероятности и индексы: доли от 0 до 1.

Данные являются сценарными оценками для калибровки модели.
"""

MODEL_YEAR = 2023

# ------------------------------------------------------------
# 1. Регионы
# ------------------------------------------------------------

REGIONS = {
    "Moscow": {
        "name": "Москва",
        "grp_bln_rub": 32_339.0,
        "labor_force_mln": 7.20,
        "sector_shares": {
            "software": 0.08,
            "science": 0.13,
            "construction": 0.03,
            "other": 0.76,
        },
        "sector_ai_intensity": {
            "software": 0.90,
            "science": 0.75,
            "construction": 0.45,
            "other": 0.35,
        },
        "technology_readiness": {
            "infrastructure": 0.92,
            "rnd": 0.95,
            "innovation": 0.90,
            "human_capital": 0.90,
            "resilience": 0.85,
        },
        "digital_gap": 0.08,
        "gini_coefficient": 0.38,
        "initial_ai_capital": 2.0,
        "annual_ai_investment": 0.35,
    },

    "KhMAO": {
        "name": "Ханты-Мансийский автономный округ — Югра",
        "grp_bln_rub": 8_671.5,
        "labor_force_mln": 0.944,
        "sector_shares": {
            "oil_gas": 0.79,
            "construction": 0.05,
            "transport": 0.04,
            "other": 0.12,
        },
        "sector_ai_intensity": {
            "oil_gas": 0.65,
            "construction": 0.40,
            "transport": 0.45,
            "other": 0.25,
        },
        "technology_readiness": {
            "infrastructure": 0.68,
            "rnd": 0.45,
            "innovation": 0.50,
            "human_capital": 0.60,
            "resilience": 0.75,
        },
        "digital_gap": 0.25,
        "gini_coefficient": 0.42,
        "initial_ai_capital": 1.0,
        "annual_ai_investment": 0.20,
    },

    "Tatarstan": {
        "name": "Республика Татарстан",
        "grp_bln_rub": 4_500.0,
        "labor_force_mln": 2.10,
        "sector_shares": {
            "oil_gas": 0.25,
            "manufacturing": 0.20,
            "construction": 0.08,
            "trade": 0.11,
            "other": 0.36,
        },
        "sector_ai_intensity": {
            "oil_gas": 0.60,
            "manufacturing": 0.55,
            "construction": 0.45,
            "trade": 0.50,
            "other": 0.30,
        },
        "technology_readiness": {
            "infrastructure": 0.75,
            "rnd": 0.65,
            "innovation": 0.70,
            "human_capital": 0.72,
            "resilience": 0.75,
        },
        "digital_gap": 0.18,
        "gini_coefficient": 0.37,
        "initial_ai_capital": 1.3,
        "annual_ai_investment": 0.25,
    },

    "Krasnodar": {
        "name": "Краснодарский край",
        "grp_bln_rub": 4_772.0,
        "labor_force_mln": 2.90,
        "sector_shares": {
            "construction": 0.09,
            "agriculture": 0.11,
            "trade": 0.15,
            "transport": 0.10,
            "other": 0.55,
        },
        "sector_ai_intensity": {
            "construction": 0.45,
            "agriculture": 0.40,
            "trade": 0.50,
            "transport": 0.45,
            "other": 0.30,
        },
        "technology_readiness": {
            "infrastructure": 0.70,
            "rnd": 0.45,
            "innovation": 0.55,
            "human_capital": 0.60,
            "resilience": 0.70,
        },
        "digital_gap": 0.22,
        "gini_coefficient": 0.38,
        "initial_ai_capital": 1.1,
        "annual_ai_investment": 0.22,
    },
}


# ------------------------------------------------------------
# 2. Компании
# ------------------------------------------------------------

FIRMS = {
    # Москва: разработка программного обеспечения
    "MSK_SOFTWARE": {
        "region_id": "Moscow",
        "industry": "Разработка программного обеспечения",
        "annual_revenue_mln_rub": 2_500.0,
        "employees": 450,
        "ai_adoption": 0.80,

        # Эффекты ИИ
        "revenue_gain_share": 0.06,
        "opex_saving_mln_rub": 180.0,
        "base_failure_prob": 0.08,
        "ai_failure_prob": 0.03,
        "loss_per_event_mln_rub": 25.0,
        "cycle_time_saving_months": 1.5,
        "monthly_product_margin_mln_rub": 90.0,

        # Стоимость ИИ
        "annual_ai_tasks": 1_200_000,
        "attempt_cost_rub": 3.0,
        "retries": 1.10,
        "human_check_share": 0.08,
        "human_check_cost_rub": 350.0,
        "accepted_quality_share": 0.97,
        "error_cost_rub": 2_000.0,
        "fixed_ai_cost_mln_rub": 45.0,

        # Риски
        "substitution_rate": 0.10,
        "augmentation_rate": 0.85,
        "algorithmic_bias": 0.03,
        "privacy_risk": 0.15,
    },

    # Москва: научная деятельность и R&D
    "MSK_SCIENCE": {
        "region_id": "Moscow",
        "industry": "Научные исследования и разработки",
        "annual_revenue_mln_rub": 1_800.0,
        "employees": 600,
        "ai_adoption": 0.65,

        "revenue_gain_share": 0.05,
        "opex_saving_mln_rub": 140.0,
        "base_failure_prob": 0.10,
        "ai_failure_prob": 0.05,
        "loss_per_event_mln_rub": 40.0,
        "cycle_time_saving_months": 2.5,
        "monthly_product_margin_mln_rub": 60.0,

        "annual_ai_tasks": 500_000,
        "attempt_cost_rub": 8.0,
        "retries": 1.25,
        "human_check_share": 0.20,
        "human_check_cost_rub": 700.0,
        "accepted_quality_share": 0.94,
        "error_cost_rub": 5_000.0,
        "fixed_ai_cost_mln_rub": 60.0,

        "substitution_rate": 0.08,
        "augmentation_rate": 0.80,
        "algorithmic_bias": 0.05,
        "privacy_risk": 0.25,
    },

    # ХМАО: добыча нефти и газа
    "KHMAO_OIL_GAS": {
        "region_id": "KhMAO",
        "industry": "Добыча нефти и газа",
        "annual_revenue_mln_rub": 180_000.0,
        "employees": 12_000,
        "ai_adoption": 0.55,

        "revenue_gain_share": 0.015,
        "opex_saving_mln_rub": 3_200.0,
        "base_failure_prob": 0.06,
        "ai_failure_prob": 0.025,
        "loss_per_event_mln_rub": 450.0,
        "cycle_time_saving_months": 0.8,
        "monthly_product_margin_mln_rub": 2_500.0,

        "annual_ai_tasks": 250_000,
        "attempt_cost_rub": 12.0,
        "retries": 1.20,
        "human_check_share": 0.25,
        "human_check_cost_rub": 900.0,
        "accepted_quality_share": 0.95,
        "error_cost_rub": 25_000.0,
        "fixed_ai_cost_mln_rub": 350.0,

        "substitution_rate": 0.12,
        "augmentation_rate": 0.70,
        "algorithmic_bias": 0.04,
        "privacy_risk": 0.30,
    },

    # Татарстан: добыча нефти и газа
    "TAT_OIL_GAS": {
        "region_id": "Tatarstan",
        "industry": "Добыча нефти и газа",
        "annual_revenue_mln_rub": 95_000.0,
        "employees": 8_000,
        "ai_adoption": 0.50,

        "revenue_gain_share": 0.015,
        "opex_saving_mln_rub": 1_700.0,
        "base_failure_prob": 0.07,
        "ai_failure_prob": 0.03,
        "loss_per_event_mln_rub": 300.0,
        "cycle_time_saving_months": 0.7,
        "monthly_product_margin_mln_rub": 1_300.0,

        "annual_ai_tasks": 180_000,
        "attempt_cost_rub": 10.0,
        "retries": 1.20,
        "human_check_share": 0.22,
        "human_check_cost_rub": 750.0,
        "accepted_quality_share": 0.94,
        "error_cost_rub": 20_000.0,
        "fixed_ai_cost_mln_rub": 220.0,

        "substitution_rate": 0.13,
        "augmentation_rate": 0.68,
        "algorithmic_bias": 0.05,
        "privacy_risk": 0.28,
    },

    # Москва: строительство и развитие территорий
    "MSK_CONSTRUCTION": {
        "region_id": "Moscow",
        "industry": "Строительство и развитие территорий",
        "annual_revenue_mln_rub": 45_000.0,
        "employees": 3_500,
        "ai_adoption": 0.45,

        "revenue_gain_share": 0.02,
        "opex_saving_mln_rub": 700.0,
        "base_failure_prob": 0.09,
        "ai_failure_prob": 0.04,
        "loss_per_event_mln_rub": 180.0,
        "cycle_time_saving_months": 1.2,
        "monthly_product_margin_mln_rub": 650.0,

        "annual_ai_tasks": 120_000,
        "attempt_cost_rub": 6.0,
        "retries": 1.18,
        "human_check_share": 0.18,
        "human_check_cost_rub": 600.0,
        "accepted_quality_share": 0.93,
        "error_cost_rub": 12_000.0,
        "fixed_ai_cost_mln_rub": 120.0,

        "substitution_rate": 0.20,
        "augmentation_rate": 0.60,
        "algorithmic_bias": 0.06,
        "privacy_risk": 0.22,
    },

    # Краснодарский край: строительство и развитие территорий
    "KRD_CONSTRUCTION": {
        "region_id": "Krasnodar",
        "industry": "Строительство и развитие территорий",
        "annual_revenue_mln_rub": 28_000.0,
        "employees": 2_800,
        "ai_adoption": 0.35,

        "revenue_gain_share": 0.02,
        "opex_saving_mln_rub": 420.0,
        "base_failure_prob": 0.10,
        "ai_failure_prob": 0.05,
        "loss_per_event_mln_rub": 120.0,
        "cycle_time_saving_months": 1.0,
        "monthly_product_margin_mln_rub": 380.0,

        "annual_ai_tasks": 80_000,
        "attempt_cost_rub": 5.0,
        "retries": 1.20,
        "human_check_share": 0.20,
        "human_check_cost_rub": 500.0,
        "accepted_quality_share": 0.92,
        "error_cost_rub": 9_000.0,
        "fixed_ai_cost_mln_rub": 80.0,

        "substitution_rate": 0.22,
        "augmentation_rate": 0.55,
        "algorithmic_bias": 0.07,
        "privacy_risk": 0.20,
    },
}


# ------------------------------------------------------------
# 3. Типовые работники для расчёта уровня «люди»
# ------------------------------------------------------------

PERSONS = {
    "MSK_SOFTWARE_WORKER": {
        "region_id": "Moscow",
        "firm_id": "MSK_SOFTWARE",
        "base_task_time_hours": 1.00,
        "ai_task_time_hours": 0.65,
        "hourly_wage_rub": 1_800.0,
        "annual_tasks": 1_700,
        "base_conversion": 0.04,
        "ai_conversion": 0.05,
        "leads": 300,
        "average_check_rub": 250_000,
        "substitution_rate": 0.10,
        "augmentation_rate": 0.85,
        "ai_skill_level": 0.85,
        "base_employment_prob": 0.97,
        "sensitive_data_share": 0.30,
        "consent_quality": 0.75,
        "algorithmic_bias": 0.03,
        "manipulation_risk": 0.15,
        "autonomy_loss": 0.15,
    },

    "MSK_SCIENCE_WORKER": {
        "region_id": "Moscow",
        "firm_id": "MSK_SCIENCE",
        "base_task_time_hours": 1.00,
        "ai_task_time_hours": 0.70,
        "hourly_wage_rub": 1_500.0,
        "annual_tasks": 1_500,
        "base_conversion": 0.03,
        "ai_conversion": 0.04,
        "leads": 100,
        "average_check_rub": 500_000,
        "substitution_rate": 0.08,
        "augmentation_rate": 0.80,
        "ai_skill_level": 0.75,
        "base_employment_prob": 0.96,
        "sensitive_data_share": 0.40,
        "consent_quality": 0.70,
        "algorithmic_bias": 0.05,
        "manipulation_risk": 0.15,
        "autonomy_loss": 0.20,
    },

    "KHMAO_OIL_GAS_WORKER": {
        "region_id": "KhMAO",
        "firm_id": "KHMAO_OIL_GAS",
        "base_task_time_hours": 1.00,
        "ai_task_time_hours": 0.80,
        "hourly_wage_rub": 1_200.0,
        "annual_tasks": 1_800,
        "base_conversion": 0.00,
        "ai_conversion": 0.00,
        "leads": 0,
        "average_check_rub": 0,
        "substitution_rate": 0.12,
        "augmentation_rate": 0.70,
        "ai_skill_level": 0.45,
        "base_employment_prob": 0.96,
        "sensitive_data_share": 0.45,
        "consent_quality": 0.55,
        "algorithmic_bias": 0.04,
        "manipulation_risk": 0.15,
        "autonomy_loss": 0.25,
    },

    "TAT_OIL_GAS_WORKER": {
        "region_id": "Tatarstan",
        "firm_id": "TAT_OIL_GAS",
        "base_task_time_hours": 1.00,
        "ai_task_time_hours": 0.82,
        "hourly_wage_rub": 950.0,
        "annual_tasks": 1_800,
        "base_conversion": 0.00,
        "ai_conversion": 0.00,
        "leads": 0,
        "average_check_rub": 0,
        "substitution_rate": 0.13,
        "augmentation_rate": 0.68,
        "ai_skill_level": 0.42,
        "base_employment_prob": 0.96,
        "sensitive_data_share": 0.42,
        "consent_quality": 0.58,
        "algorithmic_bias": 0.05,
        "manipulation_risk": 0.15,
        "autonomy_loss": 0.25,
    },

    "MSK_CONSTRUCTION_WORKER": {
        "region_id": "Moscow",
        "firm_id": "MSK_CONSTRUCTION",
        "base_task_time_hours": 1.00,
        "ai_task_time_hours": 0.80,
        "hourly_wage_rub": 850.0,
        "annual_tasks": 1_900,
        "base_conversion": 0.02,
        "ai_conversion": 0.03,
        "leads": 80,
        "average_check_rub": 1_500_000,
        "substitution_rate": 0.20,
        "augmentation_rate": 0.60,
        "ai_skill_level": 0.45,
        "base_employment_prob": 0.95,
        "sensitive_data_share": 0.25,
        "consent_quality": 0.60,
        "algorithmic_bias": 0.06,
        "manipulation_risk": 0.20,
        "autonomy_loss": 0.25,
    },

    "KRD_CONSTRUCTION_WORKER": {
        "region_id": "Krasnodar",
        "firm_id": "KRD_CONSTRUCTION",
        "base_task_time_hours": 1.00,
        "ai_task_time_hours": 0.82,
        "hourly_wage_rub": 650.0,
        "annual_tasks": 1_900,
        "base_conversion": 0.02,
        "ai_conversion": 0.03,
        "leads": 70,
        "average_check_rub": 1_200_000,
        "substitution_rate": 0.22,
        "augmentation_rate": 0.55,
        "ai_skill_level": 0.38,
        "base_employment_prob": 0.95,
        "sensitive_data_share": 0.25,
        "consent_quality": 0.55,
        "algorithmic_bias": 0.07,
        "manipulation_risk": 0.20,
        "autonomy_loss": 0.28,
    },
}