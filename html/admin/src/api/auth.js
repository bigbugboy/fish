import request from '@/utils/requests'


function login(data) {
    return request({
        url: '/api/admin/login',
        method: 'post',
        data
    })
}



export default {
    login,

}