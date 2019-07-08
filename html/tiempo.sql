CREATE EVENT tiempo
    ON SCHEDULE EVERY 1 MINUTE
    DO DELETE FROM kiosko.nfc where unix_timestamp(fecha)<(unix_timestamp()-1*3600);
