def update_service_agreement_status(storage_path, service_agreement_id,
    status='pending'):
    conn = sqlite3.connect(storage_path)
    try:
        cursor = conn.cursor()
        cursor.execute('UPDATE service_agreements SET status=? WHERE id=?',
            (status, service_agreement_id))
        conn.commit()
    finally:
        conn.close()