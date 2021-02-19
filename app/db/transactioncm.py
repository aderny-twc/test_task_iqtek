from psycopg2.extensions import STATUS_IN_TRANSACTION


class TransactionCtx:
    """Конекстный менеджер для транзакций."""

    def __init__(self, conn):
        self.conn = conn

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn.status == STATUS_IN_TRANSACTION:
            if exc_val:
                self.conn.rollback()
            else:
                self.conn.commit()
