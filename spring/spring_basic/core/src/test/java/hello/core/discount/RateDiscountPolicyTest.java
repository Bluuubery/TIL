package hello.core.discount;

import hello.core.member.Grade;
import hello.core.member.Member;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.*;

class RateDiscountPolicyTest {

    RateDiscountPolicy discountPolicy = new RateDiscountPolicy();

    @Test
    @DisplayName("Vip는 10%할인이 적용되어야 한다")
    void vip_o (){
        //given
        Member member = new Member(1L, "memberVip", Grade.VIP);
        // when
        int discount = discountPolicy.discount(member, 10000);
        // then
        assertThat(discount).isEqualTo(1000);
    }

    @Test
    @DisplayName("Vip가 아닌 경우 할인이 적용되지 않는다")
    void vip_x (){
        //given
        Member member = new Member(2L, "memberVip", Grade.BASIC);
        // when
        int discount = discountPolicy.discount(member, 10000);
        // then
        assertThat(discount).isNotEqualTo( 1000);
    }

}