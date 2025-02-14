from decimal import *
import logging as log
d= round(Decimal('0.70') * Decimal('1.05'), 2)
print("d=",d)
round = round(.70 * 1.05, 2)
print("round=",round)
log.debug("d=%s, round=%s", d, round)
log.info("d=%s, round=%s", d, round)
log.warning("d=%s, round=%s", d, round)
log.error("d=%s, round=%s", d, round)