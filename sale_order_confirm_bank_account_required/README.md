Al confirmar un presupuesto con importe > 0€, se revisará respecto al modo de pago (payment_mode_id) el método de pago (payment_method_id) y respecto a este si está definido que requiere de una cuenta bancaria (bank_account_required), en caso de que requiere se revisará que existe una cuenta bancaria al respecto, de lo contrario mostrará un mensaje.