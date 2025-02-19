import datetime
from typing import List


class JournalEntry:
    def __init__(
            self, sl_no: int,
            account: str,
            dr_amount: float,
            cr_amount: float,
            date: datetime.datetime,
            narration: str,
            key: str
    ):
        self.sl_no = sl_no
        self.account = account
        self.dr_amount = dr_amount
        self.cr_amount = cr_amount
        self.date = date
        self.narration = narration
        self.key = key


class Journal:
    def __init__(self, entries: List[JournalEntry] = None):
        self.entries: List[JournalEntry] = [] if entries is None else entries
