from model_input_data import REGIONS, FIRMS, PERSONS
from levels import Region, Firm, Person

def build_regions():
    regions = []

    for region_id, d in REGIONS.items():
        regions.append(Region(
            region_id=region_id,
            sector_shares=d["sector_shares"],
            sector_ai_intensity=d["sector_ai_intensity"],
            infrastructure_index=d["technology_readiness"]["infrastructure"],
            rnd_index=d["technology_readiness"]["rnd"],
            innovation_index=d["technology_readiness"]["innovation"],
            human_capital_index=d["technology_readiness"]["human_capital"],
            resilience_index=d["technology_readiness"]["resilience"],
            labor=d["labor_force_mln"],
            capital=d["grp_bln_rub"] / 100,
            human_capital=d["technology_readiness"]["human_capital"],
            initial_ai_capital=d["initial_ai_capital"],
            annual_ai_investment=d["annual_ai_investment"],
            digital_gap=d["digital_gap"],
            gini_coefficient=d["gini_coefficient"],
        ))

    return regions


def build_firms():
    firms = []

    for firm_id, d in FIRMS.items():
        firms.append(Firm(
            firm_id=firm_id,
            region_id=d["region_id"],
            base_revenue=d["annual_revenue_mln_rub"] * 1_000_000,
            conversion_gain=d["revenue_gain_share"],
            leads=1_000,
            average_check=d["annual_revenue_mln_rub"] * 1_000_000 / 1_000,
            opex_saving=d["opex_saving_mln_rub"] * 1_000_000,
            ai_adoption=d["ai_adoption"],
            base_failure_prob=d["base_failure_prob"],
            ai_failure_prob=d["ai_failure_prob"],
            loss_per_event=d["loss_per_event_mln_rub"] * 1_000_000,
            cycle_time_saving_months=d["cycle_time_saving_months"],
            monthly_product_margin=d["monthly_product_margin_mln_rub"] * 1_000_000,
            number_of_tasks=d["annual_ai_tasks"],
            attempt_cost=d["attempt_cost_rub"],
            retries=d["retries"],
            human_check_share=d["human_check_share"],
            human_check_cost=d["human_check_cost_rub"],
            accepted_quality_share=d["accepted_quality_share"],
            error_cost=d["error_cost_rub"],
            fixed_ai_cost=d["fixed_ai_cost_mln_rub"] * 1_000_000,
        ))

    return firms


def build_persons():
    persons = []

    for person_id, d in PERSONS.items():
        persons.append(Person(
            person_id=person_id,
            region_id=d["region_id"],
            base_task_time=d["base_task_time_hours"],
            ai_task_time=d["ai_task_time_hours"],
            hourly_wage=d["hourly_wage_rub"],
            annual_tasks=d["annual_tasks"],
            base_conversion=d["base_conversion"],
            ai_conversion=d["ai_conversion"],
            leads=d["leads"],
            average_check=d["average_check_rub"],
            substitution_rate=d["substitution_rate"],
            augmentation_rate=d["augmentation_rate"],
            ai_skill_level=d["ai_skill_level"],
            base_employment_prob=d["base_employment_prob"],
            sensitive_data_share=d["sensitive_data_share"],
            consent_quality=d["consent_quality"],
            algorithmic_bias=d["algorithmic_bias"],
            manipulation_risk=d["manipulation_risk"],
            autonomy_loss=d["autonomy_loss"],
        ))

    return persons
