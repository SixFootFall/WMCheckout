from ca.exceptions import PromotionalRuleError
from typing import List
from ca.repositories.interfaces import IPromotionalRuleRepository
from ca.entities.promotional_rule import PromotionalRule


class MemoryPromotionalRuleRepository(IPromotionalRuleRepository):
    def __init__(self) -> None:
        self.entities: List[PromotionalRule] = []

    def _validate(self, rule: PromotionalRule):
        for entity in self.entities:
            if (
                entity.discount_type == rule.discount_type
                and entity.product == rule.product
                and entity.target_quantity == rule.target_quantity
            ):
                raise PromotionalRuleError(
                    f"""Rule with type:{rule.discount_type}, 
                        product:{rule.product}, 
                        target_quantity: {rule.target_quantity} 
                        already exists in repository"""
                )

    def create(
        self, name, discount_type, product, target_quantity, measure, discount_amount
    ) -> PromotionalRule:
        rule = PromotionalRule(
            name, discount_type, product, target_quantity, measure, discount_amount
        )
        self._validate(rule)
        self.entities.append(rule)
        return rule

    def list(self) -> List[PromotionalRule]:
        return self.entities