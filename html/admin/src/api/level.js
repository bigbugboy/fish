import request from '@/utils/requests'


const url = '/api/admin/level'


function getLevel(params) {
    return request({
        url: url,
        method: 'get',
        params: params
    })
}



export default {
    getLevel,

}