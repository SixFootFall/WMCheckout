from ca.exceptions import PromotionalRuleError
from typing import List
from ca.repositories.interfaces import IPromotionalRuleRepository
from ca.entities.promotional_rule import PromotionalRule


class MemoryPromotionalRuleRepository(IPromotionalRuleRepository):
    def __init__(self) -> None:
        self.entities: List[PromotionalRule] = []

    def create(
        self, name, discount_type, product, target_quantity, measure, discount_amount
    ) -> PromotionalRule:
        rule = PromotionalRule(
            name, discount_type, product, target_quantity, measure, discount_amount
        )
        self.entities.append(rule)
        return rule

    def list(self) -> List[PromotionalRule]:
        return self.entities