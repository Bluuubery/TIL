package jpabook.jpashop.exception;

public class NotEnouchStockException extends RuntimeException {
    public NotEnouchStockException() {
        super();
    }

    public NotEnouchStockException(String message) {
        super(message);
    }

    public NotEnouchStockException(String message, Throwable cause) {
        super(message, cause);
    }

    public NotEnouchStockException(Throwable cause) {
        super(cause);
    }

}
