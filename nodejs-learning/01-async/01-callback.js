// 回调方式 - 传统写法
function fetchUserCallback(id, callback) {
  setTimeout(() => {
    if (id > 0) {
      callback(null, { id, name: `User ${id}` })
    } else {
      callback(new Error('Invalid ID'), null)
    }
  }, 1000)
}

// 使用
console.log('开始...')

fetchUserCallback(1, (err, user) => {
  if (err) {
    console.error('错误:', err.message)
    return
  }
  console.log('获取到用户:', user)
})

console.log('请求已发出，等待回调...')
